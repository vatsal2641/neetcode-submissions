class TimeMap:

    def __init__(self):
        self.hash_ = defaultdict()


    def set(self, key: str, value: str, timestamp: int) -> None:   
        if key not in self.hash_:
            self.hash_[key] = {}
        
        self.hash_[key][timestamp]  = value

        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.hash_:
            return ""
        timestamp_list = list(self.hash_[key].keys())
        req_timestamp = -float('inf')

        l = 0
        h = len(timestamp_list)-1

        if timestamp_list[h] <= timestamp:
            req_timestamp = timestamp_list[h]

        elif timestamp_list[0]> timestamp:
            return ""

        else:
            while l<=h:
                mid = (l+h)//2

                if timestamp_list[mid] == timestamp:
                    req_timestamp = timestamp_list[mid]
                    return self.hash_[key][req_timestamp]
                
                elif timestamp_list[mid] > timestamp:
                    h = mid-1
                
                else:
                    req_timestamp = max(req_timestamp, timestamp_list[mid])
                    l = mid+1
        
    
        
        return self.hash_[key][req_timestamp]
            


