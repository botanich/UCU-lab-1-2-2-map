import time
import movie_locations_parsing

def main():
    try:
        year = int(input("Please enter a year you would like" +
                         "to have a map for: "))
        latitude, longitude = map(int, input("Please enter your" +
            "location (format: \"*latitude*, *longitude*\"): ").split(', '))
        print("Map is generating, please wait...")

        #

        print("Finished. Please have a look at the map \"" + str(year) +
              "_movies_map.html\"")

    except:
        print("You caught an exception. Check your inputs and rerun" +
              "the program")
        time.sleep(1)
        input("Press any key to close the program")


if __name__ == "__main__":
    main()
