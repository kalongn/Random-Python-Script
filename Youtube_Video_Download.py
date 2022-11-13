import pytube

def main():
    url = input("Enter youtube video url: ")
    path = "" #insert your filePath (Absolute Path) Here.
    pytube.YouTube(url).streams.get_highest_resolution().download(path)

if __name__ == "__main__":
    main()