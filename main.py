from Scripts import circles
from Scripts import sinelines
from Scripts import spirograph
from Scripts import fieldsquare

basepath = "images/"


def main():
    script = "fieldsquare"

    if script == "circles":
        circles.circle()

    elif script == "sineline":
        sinelines.sineline()

    elif script == "spirograph":
        spirograph.spirograph()

    elif script == "fieldsquare":
        fieldsquare.fieldsquare()

    else:
        print("No matching script")


if __name__ == "__main__":
    main()
