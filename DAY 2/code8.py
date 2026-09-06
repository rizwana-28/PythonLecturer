color=input("Enter color: ")

match color:
    case "red":
        print("stop")
    case "yellow":
        print("wait")
    case "green":
        print("go")
    case _:                #if any case does not match then this case will be executed
        print("invalid color")