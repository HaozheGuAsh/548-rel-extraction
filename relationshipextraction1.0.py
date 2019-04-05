import abc

class RelationExtractionModel():

	def __init__(self):
		pass


	# Any shared data strcutures or methods should be defined as part of the parent class.
	# KRC. eg tokenize(), read_evaluation_dataset()
	
	# A list of shared arguments should be defined for each of the following methods and replace (or precede) *args.
	
	# The output of each of the following methods should be defined clearly and shared between all methods implemented by members of the group. 



	@classmethod
	@abc.abstractmethod
	def read_dataset(self,InputFile, *args, **kwargs):  # <--- common ACROSS ALL classes
		"""
		Read's a dataset to be used for training

		Args:
			InputFile: Filepath with list of files to be used.

		Returns: (optional)
			data from file

		"""
		pass


	@classmethod
	@abc.abstractmethod
	#-----optional for whoever requires data pre-processing
	def data_preprocess(self,inputData, *args, **kwargs):
		"""
		data cleaning techniques used like lemmatization, count vectorizer .......

		Args: 
			inputData - Raw data to tokenize

		Returns:
			Formatted data for further use.
		"""
		pass 


	@classmethod
	@abc.abstractmethod
	def tokenize(self,inputData,ngram=None, *args, **kwargs):  # <--- common ACROSS ALL classes
		"""
		Tokenizes dataset using Stanford Core NLP ( calling server or the API)

		Args:
			inputData: str or [str]. data to tokenize
			ngram: mention the size of the token combinations

		Returns:
			tokenized version of data
		"""
		pass

	@classmethod
	@abc.abstractmethod
	def train(self,trainData, *args, **kwargs):  #<--- implemented PER class
		"""
		Trains a model on the given training data

		Args:
			trainData: post-processed data to be trained.

		Returns: (Optional)
			ret: trained model in applicable formats.
				 or None if the model is stored internally. 

		"""
		pass


	@classmethod
	@abc.abstractmethod
	def predict(self,testData,trainedModel=None, *args, **kwargs):  #<--- implemented PER class...format of output??? 
		"""
		Predicts on the given input data using the given trained model

		Args:
			testData: test the model and predict the result.
			trainedModel: the trained model from the method - def train().
						  None if store trained model internally.


		Returns:
			ret: [tuple], list of tuples. 
				(Eg - Entity 1, Relation, Entity 2)

		"""
		pass

	@classmethod
	@abc.abstractmethod
	def evaluate(self, *args, **kwargs):
		"""
		Evaluates the result based on the benchmark dataset and the evauation metrics  [Precision,Recall,F1, or others...]

		Returns:
			metrics: tuple with (p,r,f1) or similar...

		"""
		pass