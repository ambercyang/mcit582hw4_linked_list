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
      self.hash = self.calc_hash()
   
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
    
M4BlockChain.append(create_genesis_block())


# In[6]:


# write a function `next_block` to generate a block
def next_block(last_block):
    new_block = Block
    pass


# In[10]:


# append 5 blocks to the blockchain
def app_five(block_list):
    
    previous_block = block_list[-1]
    
    for i in range(1,5):
        index = block_list[-1].index+1
        content = "this is block "+str(index)
        previous_hash = block_list[-1].calc_hash()
        block_list.append(Block(index, timestamp=datetime.now(), content=content, previous_hash=previous_hash))
    
    pass


# In[11]:


M4BlockChain.append(app_five(M4BlockChain))


# In[14]:


print("this is the second block:", M4BlockChain[1].content)


# In[ ]:




