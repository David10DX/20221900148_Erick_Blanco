import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Realizado por Erick David Blanco Santos/ cta: 20221900148
#BubbleSort
def bubbleSort(arr):
    n = len(arr)
    x = 0
    swapped = False
    for i in range(n-1):
       
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                for i in range(len(arr)):
                    #print("% d" % arr[i], end=" ")
                    print( arr[i], end=" ")
                print("")
                
            if not swapped:
                return
    for y in range(2, n+2):        
        sheet.update_cell(y,3,arr[x])
        x += 1

   
#Insertion Sort                
def insertionSort(arr):
    n = len(arr)
    x = 0 
    if (n := len(arr)) <= 1:
      return
    for i in range(1, n):
         
        key = arr[i]
 
        
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        print(arr)
        print("")
        
    for y in range(2, n+2):        
        sheet.update_cell(y,5,arr[x])
        x += 1

#Selection Sort        
def selectionSort(array, size):
    x = 0
    n = len(arr)
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])
        print(arr)
        print("")
        
    for y in range(2, n+2):        
        sheet.update_cell(y,4,arr[x])
        x += 1  
        

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_services.json',scope)

client = gspread.authorize(creds)

sheet = client.open('PythonSheets').sheet1
arr = []
for n in range(2,12):
    arr.append(sheet.cell(n,1).value)#, sheet.cell(3,1).value, sheet.cell(4,1).value, sheet.cell(5,1).value, sheet.cell(6,1).value, sheet.cell(7,1).value, sheet.cell(8,1).value, sheet.cell(9,1).value, sheet.cell(10,1).value, sheet.cell(11,1).value]
    
for i in range(len(arr)):
    arr[i] = int(arr[i])
size = len(arr)

print("1.Bubble Sort")
print("2.Selection Sort")
print("3.Insertion Sort")
print("x.Salir")
c = input("Elija una opción: ")
if c == 1 or c == "1":
    bubbleSort(arr)
elif c == 2 or c == "2":
    selectionSort(arr, size)
elif c == 3 or c == "3":
    insertionSort(arr)
else:
    print("Su opción no es valida")
print("")
print("")
print("")    



