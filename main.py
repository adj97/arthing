import circles

basepath = "images/"


def main():
    script = "circles"
    executed = False

    if script == "circles":
        circles.circle()
        executed = True

    if executed:
        print("Executed script: " + script)
    else:
        print("No matching script")


if __name__ == "__main__":
    main()
