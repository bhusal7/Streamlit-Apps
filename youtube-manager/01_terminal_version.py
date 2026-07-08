import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
        # return f"Exception occur as {Err}"

    # finally:
    #     pass


def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        # is return key word is necessary ..?
        json.dump(videos, file)
        
        
        
        

def list_all_vdoS(videos):
    print('\n')
    print("*" * 195)
    for i, video in enumerate(videos, start = 1):
        print(f"{i}. {video['Video Name']} | {video['duration']}")
        
    print('\n')
    print("*" * 195)





def add_vdo(videos):
    name_of_vdo = input("Enter the name of Video :- \n")
    duration = input("Enter the duration of video :- \n")

    videos.append({"Video Name": name_of_vdo, "duration": duration})
    save_data_helper(videos)


def update_vdo(videos):
    list_all_vdoS(videos)
    index = int(input("Enter the video number to update :- "))
    
    if 1 <= index <= len(videos):
        new_vdo_name = input("Enter a new video name :- ")
        new_time = input("Enter the new video time :- ")
        
        videos[index - 1] = {'Video Name': new_vdo_name, 'duration': new_time}
        save_data_helper(videos)
    else:
        print("Invalid index selected.")
    

def delete_vdo(videos):
    list_all_vdoS(videos)
    index = int(input("Enter the video number to delete :- "))
    
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print('Invalid video index selected.')


def main():
    videos = load_data()
    
    while True:
        
        print("\n Youtube Manager | Choose an Option.\n")
        print("1. List all Youtube Videos.\n")
        print("2. Add a Youtube Video\n")
        print("3. Update a Youtube Video details.\n")
        print("4. Delete a Youtube Video.\n")
        print("5. Exit the App.\n")
        
        ch = input("Enter your Choice :- ")
        print(videos)
        
        match ch:
            case "1":
                list_all_vdoS(videos)
            case "2":
                add_vdo(videos)
            case "3":
                update_vdo(videos)
            case "4":
                delete_vdo(videos)
            case "5":
                break
            case _:
                print("Invaild Choice! | Try Again from 1 to 4.")


if __name__ == "__main__":
    main()