import re
class SortableCIDRObject():
    def __init__(self, raw_cidr_string:str):
        self.raw_cidr_string = raw_cidr_string
        self.sort_string = __class__._make_sortable(raw_cidr_string)

    def __repr__(self):
        return f"{self.raw_cidr_string}"
   
    @staticmethod
    def _make_sortable(cidr_string:str):
        octet_list = []
        #Slice string to list based on IP/CIDR notation chars
        listified_string = re.split(r'[.]', cidr_string)
        #prune /XX if it exists
        if "/" in listified_string[3]:
            listified_string[3] = re.split(r'[/]', listified_string[3])[0]
        # pad sub-string from the left to be 3 chars
        for raw_octet in listified_string:
            octet = list(raw_octet)
            while len(octet) != 3:
                octet.insert(0, "0")
                if len(octet) < 0 or len(octet) > 5:
                    print("Something seems to have gone wrong while inserting extra 0's")
                    print(f"octet at time of error was: {octet}")
                    exit()
            octet_list.append("".join(octet))
        # concatenate the 4 sets of digits into a single string

        return "-".join(octet_list)

def sort_list(cidr_list:list(str)):
    sortable_object_list = []
    for raw_string in cidr_list:
        if "." not in raw_string:
            print(f"Error: String {raw_string} does not seem to be an IP address! Exiting")
            exit()
        active_string = SortableCIDRObject(raw_string)
        sortable_object_list.append(active_string)

    return sorted(sortable_object_list, key=lambda obj: obj.sort_string)














