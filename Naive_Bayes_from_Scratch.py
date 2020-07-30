import numpy as np 

class NaiveBayesClassifier:

    def __init__(self):
        pass

    def separate_classes(self, X, y):
        """
        Separates the dataset in to a subset of data for each class.

        Parameters:
        ------------
        X- array, list of features
        y- list, target

        Returns:
        ------------
        A dictionnary with y as keys and assigned X as values.
        """
        separated_classes = {}
        
        for i in range(len(X)):

            feature_values = X[i]
            class_name = y[i]

            if class_name not in separated_classes:
                separated_classes[class_name] = []
            separated_classes[class_name].append(feature_values)
        return separated_classes

    def stat_info(self, X):
        """
        Calculates standard deviation and mean of features.

        Parameters:
        ------------
        X- array , list of features

        Returns:
        ------------
        A dictionary with STD and Mean as keys and assigned features STD and Mean as values.
        """
        for feature in zip(*X):
            yield {
                'std' : np.std(feature),
                'mean' : np.mean(feature)
            }
    
    def fit (self, X, y):
        """
        Fits the Guassian Naive Bayes Classifier on the data

        Parameters:
        ------------
        X- array, list of features 
        y- list, target

        Returns:
        -----------
        Summary of fitted class
        """

        separated_classes =  self.separate_classes(X, y)
        self.class_summary = {}

        for class_name, feature_values in separate_classes.items():
            self.class_summary[classs_name] = {
                'prior_proba': len(feature_values)/len(X),
                'summary': [i for i in self.stat_info(feature_values)]
            }
        return self.class_summary

    def distribution(self, x, mean, std):
        """
        Calculates exponent and probability

        Parameters:
        -----------
        X- array, list of features
        mean- numpy mean method
        std- numpt std method

        Returns:
        -----------
        Guassian distribution probability
        """

        exponent = np.exp(-((x-mean)**2 / (2*std**2)))
        proba = exponent / (np.sqrt(2*np.pi)*std)

        return proba

    def predict(self, X):
        pass

    def accuracy(self, y_test, y_pred):
        pass
