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
    


# In[6]:


M4BlockChain.append(create_genesis_block())


# In[7]:


# write a function `next_block` to generate a block
def next_block(last_block):
    
    index = last_block.index+1
    content = "this is block "+str(index)
    previous_hash = last_block.calc_hash()
    new_block = Block(index = index, timestamp=datetime.now(), content=content, previous_hash=previous_hash)
    print("this is the new block: ", new_block, index)

    return new_block


# In[8]:


# append 5 blocks to the blockchain
def app_five(block_list):
    
    previous_block = block_list[-1]
    last_block = block_list[-1]
    
    if len(block_list) == 1:
        M4BlockChain[0]=next_block(last_block)
        for i in range(0,4):
            new_block = next_block(last_block)
            M4BlockChain.append(new_block)
    
    else:
        for i in range(0,5):
            new_block = next_block(last_block)
            M4BlockChain.append(new_block)
    
    pass


# In[9]:


M4BlockChain.append(app_five(M4BlockChain))


# In[12]:


print("this is the second block:", M4BlockChain[3].content)


# In[ ]:




