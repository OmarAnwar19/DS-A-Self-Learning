def ex1():
    jan_weather = {
        "jan 1": 27,
        "jan 2": 31,
        "jan 3": 23,
        "jan 4": 34,
        "jan 5": 37,
        "jan 6": 38,
        "jan 7": 29,
        "jan 8": 30,
        "jan 9": 35,
        "jan 10": 30,
    }

    total, count, max_val = 0, 0, 0

    # dictionary for our max key value pair
    max_kv = {"month": max_val}

    # loop over each key and value pair in jan_weather
    for key, value in jan_weather.items():
        # increment count, and add value to total
        count += 1
        total += value

        # if current value is larger than max
        if value > max_val:
            # set max val as current one
            max_val = value
            # set key value pair as current month and value
            max_kv = {key: value}

    # return:
    return {
        #average is total / count
        "avg": total // count,
        # max is the max_ key value pair from above
        "max": max_kv
    }


def ex2():
    nyc_weather = {
        "jan 1": 27,
        "jan 2": 31,
        "jan 3": 23,
        "jan 4": 34,
        "jan 5": 37,
        "jan 6": 38,
        "jan 7": 29,
        "jan 8": 30,
        "jan 9": 35,
        "jan 10": 30,
    }

    return {
        "jan 4": nyc_weather["jan 4"],
        "jan 9": nyc_weather["jan 9"]
    }


def ex3():
    poem = """Two roads diverged in a yellow wood,
            And sorry I could not travel both
            And be one traveler, long I stood
            And looked down one as far as I could
            To where it bent in the undergrowth;

            Then took the other, as just as fair,
            And having perhaps the better claim,
            Because it was grassy and wanted wear;
            Though as for that the passing there
            Had worn them really about the same,

            And both that morning equally lay
            In leaves no step had trodden black.
            Oh, I kept the first for another day!
            Yet knowing how way leads on to way,
            I doubted if I should ever come back.

            I shall be telling this with a sigh
            Somewhere ages and ages hence:
            Two roads diverged in a wood, and I—
            I took the one less traveled by,
            And that has made all the difference."""

    dict = {}

    # loop over each word in the poem
    for word in poem.split():
        # if the word is already in the dictionary
        if word in dict:
            # add one to the number of occurences of that word in the dictionary
            dict[word] += 1
        # otherwise, if word is not already in dictionary
        else:
            # add the key value pair to dict, with value = 1
            dict[word] = 1

    return dict


if __name__ == "__main__":
    print(ex1())
    print(ex2())
    print(ex3())
