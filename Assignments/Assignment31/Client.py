import Directory

def main():
    while True:
        print("\n" + "*"*50)
        print("---------- Directory Management System ----------")
        print("*"*50)
        print("1 : Search files with specific extension")
        print("2 : Rename file extensions")
        print("3 : Copy all files (Maintain Structure)")
        print("4 : Copy files with specific extension")
        print("0 : Exit")
        print("*"*50)

        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("Invalid input. Please enter a number (0-4).")
            continue

        if choice == 1:
            dname = input("Enter directory name: ")
            ext = input("Enter extension to search (e.g., .txt): ")
            Directory.FileSearch(dname, ext)
            print("Search completed. Check Result.log for details.")

        elif choice == 2:
            dname = input("Enter directory name: ")
            old_ext = input("Enter current extension (e.g., .txt): ")
            new_ext = input("Enter new extension (e.g., .doc): ")
            Directory.RenameFiles(dname, old_ext, new_ext)
            print("Renaming completed. Check Result.log for details.")

        elif choice == 3:
            src = input("Enter source directory: ")
            dest = input("Enter destination directory: ")
            Directory.CopyFiles(src, dest)
            print(f"All files from {src} copied to {dest}.")

        elif choice == 4:
            src = input("Enter source directory: ")
            dest = input("Enter destination directory: ")
            ext = input("Enter extension to copy (e.g., .py): ")
            Directory.CopyFilesExt(src, dest, ext)
            print(f"Filtered files (. {ext}) copied to {dest}.")

        elif choice == 0:
            print("Exiting... Thank you for using the system!")
            break

        else:
            print("Invalid option. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()