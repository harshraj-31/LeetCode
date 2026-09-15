class Solution:
    def canVisitAllRooms(self, rooms):
        # Keep track of the rooms we have already opened
        visited = set([0])
        
        # Keep a pile of keys we have found but haven't used yet
        stack = [0]
        
        while stack:
            # Take a key from the top of our pile and enter the room
            current_room = stack.pop()
            
            # Check all the new keys we find in this room
            for key in rooms[current_room]:
                if key not in visited:
                    # Mark the room as unlocked/visited
                    visited.add(key)
                    # Add the new key to our pile to check later
                    stack.append(key)
                    
        # If the number of rooms we visited equals the total number of rooms, we opened them all!
        return len(visited) == len(rooms)