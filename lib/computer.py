class Computer:
    
    all_instances = []
    
    def __init__(self, brand, model, memory_GB=8, storage_free=1000):
        self._brand = brand
        self._model = model
        self._memory_GB = memory_GB
        self._storage_free = storage_free
        Computer.all_instances.append(self)
        
    @property
    def brand(self):
        return self._brand
    
    @property
    def model(self):
        return self._model
    
    @property
    def memory_GB(self):
        return self._memory_GB
    @memory_GB.setter
    def memory_GB(self, value):
        self._memory_GB = value
    
    @property
    def storage_free(self):
        return self._storage_free
    
    @storage_free.setter
    def storage_free(self, value):
        if 0 < value <= 1000:
            self._storage_free = value
        else:
            print(f"The is maximum 1000 and the minimum is 0.")
        
    def upgrade_memory(self, RAM):
        model = RAM.get('model')
        size = RAM.get('size')
        self._memory_GB += size      
        #print(model)
        #print(size)
        #print(self._memory_GB)
        
    def is_disk_full(self, file_size):
        if self._storage_free < file_size:
            return True
        else: 
            return False
    # saves file is it fits using helper function and reduces size
    def save_file(self, file):
        if self.is_disk_full(file['size']) == False: 
            self._storage_free -= file['size']          
            return f"{file['name']} has been saved!"        
        else: 
            return f"There is not enough space on disk to save {file['name']}."
        
    def  delete_file(self, file):
        #have to save file name before deleting it from the system
        file_name = file['name']        
        del file['name']
        self._storage_free += file['size']
        return f"The file '{file_name}' has been deleted and your space is {self._storage_free}."
            
    def specs(self):
        return print(f"My PCs specs: \nFree Storage: {self._storage_free} bytes. \nFree Memory: {self._memory_GB} bytes")            
   
    @classmethod
    def brands(cls):
        #sets dont allow duplicates so we save there
        brands_list = set()
        for instance in cls.all_instances:
            brands_list.add(instance.brand)  
            #we convert it back to clean list to be returned          
        return list(brands_list)
    
    @classmethod
    def models(cls):
        #sets dont allow duplicates so we save there
        models_list = set()
        for instance in cls.all_instances:
            models_list.add(instance.model)  
            #we convert it back to clean list to be returned          
        return list(models_list)
    
    @classmethod
    def largest_memory(cls):
        memory_list = []
        for instance in cls.all_instances:
            memory_list.append(instance.memory_GB)
            return print(max(memory_list))
    
if __name__ == "__main__":
    # you can write test code here
    # or in debug.py
    pass


