'''___Daily Challenge_____________________________________________________________________________________________________________________________________'''

#____Daily Challenge : Pagination   _____

class Pagination():
    def __init__(self, items, pagesize) -> None:
        self.items = items
        self.pagesize = int(pagesize)
        self.current_page = 1
        self.total_pages = len(self.items) // self.pagesize

    def getVisibleItems(self):
        end_index = self.pagesize * self.current_page
        start_index = end_index - self.pagesize

        current_page_items = self.items[start_index:end_index]
        return current_page_items

    def prevPage(self):
        if self.current_page > 1:
            prev_page = self.current_page - 1
        else:
            prev_page = self.current_page
        print('No previous pages,It was 1st page')
        return prev_page

    def nextPage(self):
        if self.current_page < self.total_pages:
            next_page = self.current_page + 1
        else:
            next_page = self.current_page
        print('No next pages,It was last page')
        return next_page

    

    def firstPage(self):
        self.current_page = 1
        return self.current_page

    def lastPage(self):
        lastPage = self.total_pages
        return lastPage

    def goToPage(self, pageNum):
        if 1 <= pageNum <= self.total_pages:
            self.current_page = pageNum
        return self.current_page


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
print(alphabetList)

p = Pagination(alphabetList, 4)
print(p.getVisibleItems())  
print(p.nextPage())  
print(p.getVisibleItems()) 
print(p.prevPage())  
print(p.firstPage())  
print(p.lastPage())  
print(p.goToPage(3))  
print(p.getVisibleItems())  

#___________________________

