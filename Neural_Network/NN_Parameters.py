class NN_parameters:
    def __init__(self,model,model_type,epochs,batch_size):
        self.model=model
        self.model_type= model_type
        self.epochs = epochs
        self.batch_size = batch_size

    def default_model(self,model):
        self.model='relu'

    def default_model_type(self,model_type):
        self.model_type='sigmoid'

    def default_epochs(self,epochs):
        self.epochs=181

    def default_bacth_size(self,batch_size):
        self.batch_size=100