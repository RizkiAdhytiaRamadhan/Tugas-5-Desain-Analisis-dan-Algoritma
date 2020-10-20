#!/usr/bin/env python
# coding: utf-8

# # Divide & Conquor
# ## I. Inversi dalam suatu array
# Menghitung berapa banyak perubahan yang harus dilakukan untuk mengubah array menjadi
# bentuk yang urut. Ketika array sudah diurutkan, berarti memerlukan 0 inversi.

# In[8]:


def countInversion(arr):
    result=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                result+=1
    return result


# In[9]:


arr=[21, 70, 36, 14, 25]


# In[10]:


result=countInversion(arr)
print(result)


# In[84]:


# Hitung Inversi dengan divide don conquer
def countInversion(arr):
    icount=0
    if len(arr)<=1:
        return icount
    
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    icount+=countInversion(left)
    icount+=countInversion(right)
    i=j=k=0 
    
    #print(Left)
    #print(right)
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            #print(Left[i],right[j])
            arr[k]=right[j]
            j+=1
            icount+=(mid-i)
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
        
    return icount


# In[88]:


arr=[1,20,6,4,5]
result=countInversion(arr)
print(result)


# ## II.	Maximum Subarray Sum
# Mencari hasil penjumlahan terbesar dari suatu array yang isinya nilai negatif dan positif. Misal suatu array isinya {-2, -5, 6, -2, -3, 1, 5, -6}, maka penjumlahan terbesar disusun dari {6, -2, -3, 1, 5} = 7
# 

# In[76]:


# Tanpa divide dan conquer 
def maxSubSum(arr): 
    max_so_far=0 
    max_ending_here=0 
    for i in range(len(arr)): 
        max_ending_here+=arr[i] 
        if max_ending_here>max_so_far: 
            max_so_far=max_ending_here 
        if max_ending_here<0: 
            max_ending_here=0 
    return max_so_far 


# In[77]:


arr=[-2, -5, 6, -2, -3, 1, 5, -6]
result=maxSubSum(arr)
print(result) 


# In[86]:


# Menggunakan Divide and Conquer 
def maxCrossingSum(arr,low,mid,high):
    result=0; leftSum=float('-infinity')
    for i in range(mid,low-1,-1):
        result+=arr[i]
        if result>leftSum:
            leftSum=result
    result=0; rightSum=float('-infinity')
    for i in range(mid+1,high+1):
        result+=arr[i]
        if result>rightSum:
            rightSum=result
    return leftSum+rightSum


def maxSum(arr,low,high):
    if low==high:
        return arr[low] 
    mid=(low+high)//2
    return max(maxSum(arr,low,mid),maxSum(arr,mid+1,high),maxCrossingSum(arr,low,mid,high)) 


# In[87]:


arr=[-2, -5, 6, -2, -3, 1, 5, -6] 
result=maxSum(arr,0,len(arr)-1)
print(result)


# ## III.	Longest Common Prefix
# Mencari potongan suku kata (prefix) yang sama dan terpanjang
# 

# In[10]:


def commonPrefix(str1,str2):
    n1=len(str1);n2=len(str2)
    i,j=0,0
    s=""
    while i<n1 and j<n2:
        if str1[i]==str2[j]:
            s+=str1[i]
            i+=1
            j+=1
        else:
            break
    return s
    


# In[11]:


def longestCommonPrefix(arr,low,high):
    if low==high:
        return arr[low]
    mid=(low+high)//2
    result1=longestCommonPrefix(arr,low,mid)
    result2=longestCommonPrefix(arr,mid+1,high)
    result=commonPrefix(result1,result2)
    return result


# In[12]:


arr=['geeksforgeeks', 'geeks', 'geek', 'geezer']


# In[13]:


result=longestCommonPrefix(arr,0,len(arr)-1)


# In[14]:


print(result)


# In[15]:


arr=["apple", "ape", "april"]
result=longestCommonPrefix(arr,0,len(arr)-1)
print(result)


# ## IV.	Median dua array urut sama ukuran
# Mencari nilai tengah dari dua array yang berurutan nilainya, dan ukurannya sama

# In[23]:


# Median dori duo array dengan divide don conquer
def medianOfArray(arr1,arr2,n):
    m1=-1
    #first number
    m2=-1
    #second Number
    count=0
    i=j=0
    while count<n+1:
        count+=1
        if i==n: # i==S index error if orrl[i]corr2(j] is checked
            m1=m2
            m2=arr2[0]
            break
        if j==n:
            m1=m2
            m2=arr1[0]
            break
        if arr1[i]<arr2[j]:
            m1=m2
            m2=arr1[i]
            i+=1
        else:
            m1=m2
            m2=arr2[j]
            j+=1
    return (m1+m2)//2 


# In[24]:


arr1=[1, 12, 15, 26, 38]
arr2=[2, 13, 17, 30, 45] 


# In[25]:


print(medianOfArray(arr1,arr2,len(arr1)))


# ## V.	Median dua array urut berbeda ukuran
# Mencari nilai tengah array yang berurutan, namun ukurannya berbeda

# In[26]:


# Floor in sorted array
def floorSorted(arr,low,high,x):
    #print(low,high)
    if low>high:
        return -1
    
    if arr[low]>x:
        #print("inside")
        return -1
    
    if arr[high]<=x:
        return arr[high]
    
    mid=(low+high)//2 
    
    if arr[mid]==x:
        return arr[mid]
    
    if mid>0 and x>=arr[mid-1] and arr[mid]>x:
        return arr[mid-1]
    
    if mid<high and x<arr[mid+1] and x>=arr[mid]:
        return arr[mid]
    
    if x>arr[mid]:
        return floorSorted(arr,mid+1,high,x)
    
    else:
        return floorSorted(arr,low,mid-1,x) 


# In[27]:


arr=[1,2,8,10,12,14,19]


# In[28]:


x=5


# In[29]:


print(floorSorted(arr,0,len(arr)-1,x))


# ## VI.	Nilai terdekat
# Mencari nilai terdekat suatu angka dalam suatu array

# In[30]:


# Mencari niLai terdekat dengan metode divide don conquer
def closestNumber(arr,low,high,x):
    if low>high:
        return -1
    if arr[high]<=x:
        return arr[high]
    if arr[low]>=x:
        return arr[low]
    mid=(low+high)//2
    if arr[mid]==x:
        return arr[mid]
    abs_mid=abs(arr[mid]-x)
    if mid>0:
        abs_left=abs(arr[mid-1]-x)
        if abs_left<abs_mid:
            return closestNumber(arr,low,mid-1,x)
    if mid<high:
        abs_right=abs(arr[mid+1]-x)
        if abs_right<abs_mid:
            return closestNumber(arr,mid+1,high,x)
    #print('after')
    return arr[mid] 


# In[31]:


arr=[2, 5, 6, 7, 8, 8, 9] 


# In[32]:


x = 9


# In[33]:


print(closestNumber(arr,0,len(arr)-1,x))


# ## VII.	Fixed Point
# Mencari nilai fixed point, yaitu suatu bilangan dalam array yang nilainya sama dengan urutannya dalam array. Array dimulai dari 0. Jika tidak ada yang sama, hasil akan bernilai -1.

# In[34]:


# Mencari Fixed Point dengan metode divide don conquer
def fixedPoint(arr,low,high):
    if low>high:
        return -1
    if arr[high]==high:
        return arr[high]
    if arr[low]==low:
        return arr[low]
    mid=(low+high)//2
    if arr[mid]==mid:
        return arr[mid]
    if mid>arr[mid]:
        return fixedPoint(arr,mid+1,high)
    else:
        return fixedPoint(arr,low,mid-1) 


# In[35]:


arr=[9,1,4,5,2]


# In[37]:


print(fixedPoint(arr,0,len(arr)-1))

