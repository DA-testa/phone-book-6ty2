# python3

class HashTable:  
    def __init__(self):
        self.MA = 10
        self.tab = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.MAX
    
    def get(self, key):
        hash = self.get_hash(key)
        for elemet in self.tab[hash]:
            if element[0] == key:
                return element[1]

    
    def add(self, key, value):
        hash = self.get_hash(key)
        found = False
        for i, element in enumerate(self.tab[hash]):
            if len(element)==1 and element[0] == key:
                # update element
                self.tab[hash][i] = (key,value)
                found = True
        if not found:
            # Add element
            self.tab[hash].append((key, value))
    
    def delete(self, key):
        hash = self.get_hash(key)
        for i, element in enumerate(self.tab[hash]):
            if element[0] == key:
                del self.tab[hash][i]

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

