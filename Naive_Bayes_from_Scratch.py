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
        A dictionary with STD and Mean as keys and assigned features STD and Mean as values.
        """
        for feature in zip(*X):
            yield {
                'std' : np.std(feature),
                'mean' : np.mean(feature)
            }
    
    def fit (self, X, y):
        """
        Trains the model.

        Parameters:
        ----------
        X: array-like, training features
        y: list, target variable

        Returns:
        Dictionary with the prior probability, mean, and standard deviation of each class
        """

        separated_classes = self.separate_classes(X, y)
        self.class_summary = {}

        for class_name, feature_values in separated_classes.items():
            self.class_summary[class_name] = {
                'prior_proba': len(feature_values)/len(X),
                'summary': [i for i in self.stat_info(feature_values)],
            }
        return self.class_summary

    def distribution(self, x, mean, std):
        """
        Gaussian Distribution Function

        Parameters:
        ----------
        x: float, value of feature
        mean: float, the average value of feature
        stdev: float, the standard deviation of feature

        Returns:
        A value of Normal Probability
        """

        exponent = np.exp(-((x-mean)**2 / (2*std**2)))

        return exponent / (np.sqrt(2*np.pi)*std)

    def predict(self, X):
        """
        Predicts the class.

        Parameters:
        ----------
        X: array-like, test data set

        Returns:
        -----------
        List of predicted class for each row of data set
        """
        MAPs = []

        for row in X:
            joint_proba = {}
            
            for class_name, features in self.class_summary.items():
                total_features =  len(features['summary'])
                likelihood = 1

                for idx in range(total_features):
                    feature = row[idx]
                    mean = features['summary'][idx]['mean']
                    stdev = features['summary'][idx]['std']
                    normal_proba = self.distribution(feature, mean, stdev)
                    likelihood *= normal_proba
                prior_proba = features['prior_proba']
                joint_proba[class_name] = prior_proba * likelihood

            MAP = max(joint_proba, key= joint_proba.get)
            MAPs.append(MAP)

        return MAPs

    def accuracy(self, y_test, y_pred):
        """
        Calculates model's accuracy.

        Parameters:
        ------------
        y_test: actual values
        y_pred: predicted values

        Returns:
        ------------
        A number between 0-1, representing the percentage of correct predictions.
        """

        true_true = 0

        for y_t, y_p in zip(y_test, y_pred):
            if y_t == y_p:
                true_true += 1 
        return true_true / len(y_test)
