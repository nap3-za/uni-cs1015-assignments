# Data extractor
# 03 April 2024


def location(block):
    # Your code here

    start_position = block.find(",") + 5 # After the Y-cordinate which comes after the only coma
    end_position = len(block)-5 # Before the last 4 letters, " END"

    return block[end_position:start_position:-1].title()


def temperature(block):
    # Your code here

    start_position = 6 # After "BEGIN "
    end_position = block.find("_") # Before the underscore in temp_press

    return float(block[start_position:end_position])


def x_coordinate(block):
#     # Your code here

    start_position = block.find(":")+1 # After colon
    end_position = block.find(",") # Before the first coma in the provided data

    return block[start_position:end_position]


def y_coordinate(block):
#     # Your code here

    start_position = block.find(",")+1 # After colon
    end_position = start_position + block[start_position:].find(" ") # Before the space after the y-cordinate

    return block[start_position:end_position]    


def pressure(block):
    # Your code here

    start_position = block.find("_")+1 # After the underscore
    end_position = block.find(":") # Before the colon

    return float(block[start_position:end_position])




def get_block(data):
    # Your code here

    # Get the start and end index, BEGIN & END
    useful_data_start = data.find("BEGIN")
    useful_data_end = data.find("END") + 3
    # Chop the raw data
    useful_data = data[useful_data_start:useful_data_end]
    return useful_data

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
