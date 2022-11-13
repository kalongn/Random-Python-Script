import pytube

def main():
    url = input("Enter youtube video url: ")
    path = input("Enter youtube where the video should go to (Absoltue path): ")
    pytube.YouTube(url).streams.get_highest_resolution().download(path)

if __name__ == "__main__":
    main()