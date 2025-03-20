# EXAMPLE WITH A TUPLE OF TUPLES ~ can iterate over tuples
# aTuple:((int,string), (int,string), (int,string))

'''

# Every t in aTuple
aTuple: (
    (), # t
    (), # t
    ()  # t
)

'''

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],) # each time, add a tuple of one elemet or character to the nums empty tuple
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    
    unique_words = len(words)
    return (min_n, max_n, unique_words)

tswift = ((2014,"Katy"), (2014,"Jake"), (2012,"Jake"), (2010,"Taylor"), (2008,"Joe"))
(min_year, max_year, num_people) = get_data(tswift)

print("From", min_year, "to", max_year, "Taylor Swift wrote songs about", num_people, "people")


if __name__ == "__main__":
    get_data(tswift)