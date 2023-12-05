'''___Daily Challenge_____________________________________________________________________________________________________________________________________'''

#____Daily Challenge : Pagination   _____

class Pagination():
    def __init__(self, items, pagesize) -> None:
        self.items = items
        self.pagesize = int(pagesize)
        self.current_page = 1

    def getVisibleItems(self):
        end_index = self.pagesize * self.current_page
        start_index = end_index - self.pagesize

        current_page_items = self.items[start_index:end_index]
        return current_page_items

    def nextPage(self):
        self.current_page += 1
        return self.current_page

    def prevPage(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self.current_page

    def firstPage(self):
        self.current_page = 1
        return self.current_page

    def lastPage(self):
        total_pages = len(self.items) // self.pagesize
        if len(self.items) % self.pagesize != 0:
            total_pages += 1
        self.current_page = total_pages
        return self.current_page

    def goToPage(self, pageNum):
        if 1 <= pageNum <= len(self.items) // self.pagesize + 1:
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

