class TimeMap:

    def __init__(self):
        self.hash_ = defaultdict()


    def set(self, key: str, value: str, timestamp: int) -> None:   
        if key not in self.hash_:
            self.hash_[key] = []
        
        self.hash_[key].append((timestamp, value))

        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.hash_:
            return ""
            
        timestamp_list = self.hash_[key]
        req_timestamp = -float('inf')

        l = 0
        h = len(timestamp_list)-1

        if timestamp_list[h][0] <= timestamp:
            return timestamp_list[h][1]

        elif timestamp_list[0][0]> timestamp:
            return ""

        else:
            while l<=h:
                mid = (l+h)//2

                if timestamp_list[mid][0] == timestamp:
                    return timestamp_list[mid][1]
                
                elif timestamp_list[mid][0] > timestamp:
                    h = mid-1
                
                else:
                    
                    if timestamp_list[mid][0]>req_timestamp:
                        req_timestamp = timestamp_list[mid][0]
                        req_val = timestamp_list[mid][1]

                    l = mid+1
        
    
        
        return req_val
            


