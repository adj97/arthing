from Scripts import circles
from Scripts import sinelines

basepath = "images/"


def main():
    script = "sineline"

    if script == "circles":
        circles.circle()

    elif script == "sineline":
        sinelines.sineline()

    else:
        print("No matching script")


if __name__ == "__main__":
    main()
