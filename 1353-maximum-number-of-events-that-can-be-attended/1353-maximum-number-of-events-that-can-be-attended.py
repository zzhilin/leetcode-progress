class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # greedy'
        # we can attend one event on one day, so we can scan from day one to day n(max of all endDays)
        # we will pick event with earliest end time so that we can attend more events
        # to sort by end times, we can use a min heap that saves all events' end time
        # at each day, we remove events that ended and add events start on this day
        # attend the event with earliest endTime (top of min heap)
        can_attend = 0
        total_days = max(e[1] for e in events)
        day = 1 # start

        min_hp = []
        id_map = defaultdict(list)
        for i in range(len(events)):
            id_map[events[i][0]].append(i)
        
        while day <= total_days:
            # in each day, add events start at current day to min heap
            for j in id_map[day]:
                heapq.heappush(min_hp, events[j][1])
            # remove events end at this day
            while len(min_hp) > 0 and min_hp[0] < day:
                heapq.heappop(min_hp)
            # pick earliest ended events from the rest
            if len(min_hp) > 0:
                heapq.heappop(min_hp)
                can_attend+= 1
            day += 1
            
        return can_attend