from backup_manager import BackupManager

if __name__ == "__main__":
    try:
        backup_folder = input("Enter the backup folder path: ")
        source_folder = input("Enter the source folder to backup: ")

        backup_manager = BackupManager(backup_folder)
        backup_manager.perform_backup(source_folder)

        print("Script completed.")
    except KeyboardInterrupt:
        print("\nBackup operation was interrupted.")
    except NotEnoughSpace as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
