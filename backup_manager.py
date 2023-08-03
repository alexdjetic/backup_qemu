import os
import shutil
import tarfile
import getpass
import sys
from NotEnoughSpaceException import NotEnoughSpace

class BackupManager:
    """
    A class for managing backups.
    """

    def __init__(self, backup_folder: str) -> None:
        """
        Initialize a BackupManager instance.

        :param backup_folder: The path to the backup folder.
        """
        self.backup_folder = backup_folder

    def create_backup_folder(self) -> None:
        """
        Create the backup folder if it doesn't exist.
        """
        try:
            if not os.path.exists(self.backup_folder):
                os.makedirs(self.backup_folder)
                print(f"Created backup folder: {self.backup_folder}")
        except Exception as e:
            print(f"Error creating backup folder: {str(e)}")
            sys.exit(1)

    def elevate_privileges(self) -> None:
        """
        Elevate privileges using sudo if required.
        """
        if os.name == 'posix' and os.geteuid() != 0:
            print("This operation requires elevated privileges.")
            choice = input("Do you want to elevate privileges? (y/n): ")
            if choice.lower() == 'y':
                os.execvp('sudo', ['sudo', 'python'] + sys.argv)

    def get_folder_size(self, folder_path: str) -> int:
        """
        Get the total size of a folder and its contents.

        :param folder_path: The path to the folder.
        :return: The total size in bytes.
        """
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size

    def compress_backup(self, source_folder: str, target_path: str) -> None:
        """
        Compress the source folder into a target path.

        :param source_folder: The path to the source folder.
        :param target_path: The path to save the compressed backup.
        """
        with tarfile.open(target_path, "w:gz", compresslevel=5) as tar:
            tar.add(source_folder, arcname=os.path.basename(source_folder))
        print(f"Backup compressed and saved to: {target_path}")

    def perform_backup(self, source_folder: str) -> None:
        """
        Perform a backup of a source folder.

        :param source_folder: The path to the source folder.
        """
        try:
            self.create_backup_folder()
            self.elevate_privileges()

            backup_filename = f"{os.path.basename(source_folder)}.tgz"
            backup_path = os.path.join(self.backup_folder, backup_filename)

            source_size = self.get_folder_size(source_folder)
            available_space = self.get_available_space()
            if available_space < source_size:
                raise NotEnoughSpace(available_space, source_size)

            self.compress_backup(source_folder, backup_path)
            shutil.rmtree(source_folder)  # Remove the original uncompressed folder

            print("Backup completed.")
        except KeyboardInterrupt:
            print("\nBackup operation was interrupted.")
        except NotEnoughSpace as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def get_available_space(self) -> int:
        """
        Get the available space in the backup folder.

        :return: The available space in bytes.
        """
        statvfs = os.statvfs(self.backup_folder)
        return statvfs.f_frsize * statvfs.f_bavail
