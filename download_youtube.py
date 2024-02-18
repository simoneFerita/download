from pytube import YouTube
import sys

def download_video(video_url, output_path='.', itag=None):
    try:
        yt = YouTube(video_url)


        available_streams = yt.streams.all()

        if itag is not None:

            if itag.isdigit() and int(itag) in [stream.itag for stream in available_streams]:
                selected_stream = yt.streams.get_by_itag(int(itag))
            else:
                print("Itag error. Insert number.")
                sys.exit(1)
        else:

            print("Insert number:")
            for i, stream in enumerate(available_streams, start=1):
                print(f"{i}. {stream}")

            selected_index = input("Insert number: ")

           
            if selected_index.isdigit() and int(selected_index) in range(1, len(available_streams) + 1):
                selected_stream = available_streams[int(selected_index) - 1]
            else:
                print("No correct")
                sys.exit(1)

   
        selected_stream.download(output_path)
        print(f"Download completed: {yt.title}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_youtube.py <video_url> [output_path] [itag]")
        sys.exit(1)

    video_url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else '.'
    itag = sys.argv[3] if len(sys.argv) > 3 else None

    download_video(video_url, output_path, itag)
