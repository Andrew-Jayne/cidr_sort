import re

class UnsortableCIDRObject():
    def __init__(self, raw_cidr_string:str):
        self.raw_cidr_string = raw_cidr_string
        self.sort_string = 'ffffffffffff'
    
    def __repr__(self):
        return f"{self.raw_cidr_string}"

class SortableCIDRObject():
    def __init__(self, raw_cidr_string:str):
        self.raw_cidr_string = raw_cidr_string
        self.sort_string = __class__._make_sortable(raw_cidr_string)

    def __repr__(self):
        return f"{self.raw_cidr_string}"
   
    @staticmethod
    def _make_sortable(cidr_string:str):
        octet_list = []
        #prune /XX if it exists
        if "/" in cidr_string:
            strip_list = re.split(r'[/]', cidr_string)
            cidr_string = strip_list[0]
        #Slice string to list based on IP/CIDR notation chars
        listified_string = re.split(r'[.]', cidr_string)
        # pad sub-string from the left to be 3 chars
        for raw_octet in listified_string:
            octet = list(raw_octet)
            match len(octet):
                case 1:
                    octet.insert(0, "0")
                    octet.insert(0, "0")
                case 2:
                    octet.insert(0, "0")
                case 3:
                    pass
                case _:
                    print(f"Warning: Invalid Octect: {octet}, will be set to fff")
                    octet = ["f","f","f"]
            octet_list.append("".join(octet))
        # concatenate the 4 sets of digits into a single string

        return str("-".join(octet_list))


def sort_list(cidr_list:list):
    sortable_object_list = []
    for raw_string in cidr_list:
        if "." not in raw_string:
            print(f"Warning: Invalid String: {raw_string} does not seem to be an IP address!")
            errored_string = UnsortableCIDRObject(raw_string)
            sortable_object_list.append(errored_string)
        else:
            active_string = SortableCIDRObject(raw_string)
            sortable_object_list.append(active_string)

    return sorted(sortable_object_list, key=lambda obj: obj.sort_string)


my_bad_list = ["192.168.0.1", "192.168.0.0/16", "1:15:26.666", "192.69420.0.12/64", "this is my worst string i can make ."]
print(sort_list(my_bad_list))