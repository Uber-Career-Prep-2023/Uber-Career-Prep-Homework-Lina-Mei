'''
An animal shelter that houses cats and dogs wants to ensure no pet has to wait too long for a forever home. 
Therefore, anyone who comes to adopt a pet can pick the species (cat or dog) but not the specific animal; 
they are assigned the animal of that species that has been in the shelter longest. If there are no animals 
available of the desired species, they must take the other species. You are given a list of pets in the 
shelter with their names, species, and time in the shelter at the start of a week. You receive a sequence 
of incoming people (to adopt pets) and animals (new additions to the shelter) one at a time.
Print the names and species of the pets as they are adopted out.
Example (input and output forms one sequence of sample input):

Initial Input:
Sadie, dog, 4 days
Woof, cat, 7 days
Chirpy, dog, 2 days
Lola, dog, 1 day

Approach: 2 heaps
Time complexity: O(N+M) where N represents the number of elements in the animal shelter 
and M represents the number of tuples from the sequence of incoming people and additions to the shelter
Space complexity: O(N) where N represents the number of animals in the animal shelter
Time taken: 
40 minutes

'''
import heapq

def adopt(pets, adoptions):
    cats = []
    dogs = []


    for name, pet, days in pets:
        if pet == 'dog':
            heapq.heappush(dogs, (-days, name)) # negative for max heap                
        if pet == 'cat':
            heapq.heappush(cats, (-days, name)) # negative for max heap
    results = []
    for stream in adoptions:
        name = stream[0]
        
        # for incoming pets at the adoptiong
        if len(stream) != 3:
            pet = stream[1]
            if pet == 'cat':
                heapq.heappush(cats, (cats[-1][0]+1, name))
            elif pet == 'dog':
                heapq.heappush(dogs, (dogs[-1][0]+1, name))
            continue
        
        # for incoming adoptions from people
        pet = stream[2]
        
        # adoptiong dogs
        if pet == 'dog':
            if len(dogs) > 0:
                name = heapq.heappop(dogs)[1]
                results.append((name, pet))
            elif len(cats) > 0:
                name = heapq.heappop(cats)[1]
                results.append((name, 'cat'))
                
        # adoptiong cats  
        if pet =='cat':
            if len(cats) > 0:
                name = heapq.heappop(cats)[1]
                results.append((name, pet))
            elif len(dogs) > 0:
                name = heapq.heappop(dogs)[1]
                results.append((name, 'dog'))
    return results

pets = [('Sadie', 'dog', 4), 
        ('Woof', 'cat', 7),
        ('Chirpy', 'dog', 2), 
        ('Lola', 'dog', 1)]

adoptions = [('Bob', 'person', 'dog'),  # Sadie, dog
                ('Floofy', 'cat'),   # 
                ('Ji', 'person', 'cat'), # Woof, cat
                ('Sally', 'person', 'cat'),  # Floofy, cat
                ('Ali', 'person', 'cat')] # Chirpy, dog

print(adopt(pets, adoptions)) 
