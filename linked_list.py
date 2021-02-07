#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib


# In[2]:


class Block:
    def __init__(self, index, timestamp, content, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.content = content
      self.previous_hash = previous_hash
      self.hash = self.calc_hash
   
    def calc_hash(self):
      sha = hashlib.sha256()
      sha.update(str(self.index).encode('utf-8') + 
                 str(self.timestamp).encode('utf-8') + 
                 str(self.content).encode('utf-8') + 
                 str(self.previous_hash).encode('utf-8'))
      return sha.hexdigest()


# In[3]:


M4BlockChain = []


# In[4]:


from datetime import datetime


# In[5]:


def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")
    


# In[6]:


#M4BlockChain.append(create_genesis_block())
M4BlockChain.append(create_genesis_block())


# In[7]:


# write a function `next_block` to generate a block
def next_block(last_block):
    my_index = last_block.index + 1
    my_content = "this is block "+str(my_index)
    my_timestamp = datetime.now()
    my_previous_hash = last_block.hash()
    
    new_block = Block(my_index, my_timestamp , my_content, my_previous_hash)
    print("this is the new block: ", new_block, my_index)

    return new_block


# In[8]:


# append 5 blocks to the blockchain
def app_five(block_list):
    
    for i in range(0,5):
        M4BlockChain.append(next_block(M4BlockChain[-1]))

    pass


# In[9]:


M4BlockChain.append(app_five(M4BlockChain))
print(len(M4BlockChain))


# In[10]:


print("this is the second block:", M4BlockChain[4].index)


# In[11]:





# In[ ]:




