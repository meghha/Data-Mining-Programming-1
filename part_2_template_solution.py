# Add your imports here.
# Note: only sklearn, numpy, utils and new_utils are allowed.

import numpy as np
from numpy.typing import NDArray
from typing import Any
import utils as u
import new_utils as nu
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import (
    ShuffleSplit,
    cross_validate,
    KFold,
)
# ======================================================================

# I could make Section 2 a subclass of Section 1, which would facilitate code reuse.
# However, both classes have the same function names. Better to pass Section 1 instance
# as an argument to Section 2 class constructor.


class Section2:
    def __init__(
        self,
        normalize: bool = True,
        seed: int | None = None,
        frac_train: float = 0.2,
    ):
        """
        Initializes an instance of MyClass.

        Args:
            normalize (bool, optional): Indicates whether to normalize the data. Defaults to True.
            seed (int, optional): The seed value for randomization. If None, each call will be randomized.
                If an integer is provided, calls will be repeatable.

        Returns:
            None
        """
        self.normalize = normalize
        self.seed = seed
        self.frac_train = frac_train

    # ---------------------------------------------------------

    """
    A. Repeat part 1.B but make sure that your data matrix (and labels) consists of
        all 10 classes by also printing out the number of elements in each class y and 
        print out the number of classes for both training and testing datasets. 
    """

    def partA(
        self,
    ) -> tuple[
        dict[str, Any],
        NDArray[np.floating],
        NDArray[np.int32],
        NDArray[np.floating],
        NDArray[np.int32],
    ]:
        answer = {}
        # Enter your code and fill the `answer`` dictionary

        # `answer` is a dictionary with the following keys:
        # - nb_classes_train: number of classes in the training set
        # - nb_classes_test: number of classes in the testing set
        # - class_count_train: number of elements in each class in the training set
        # - class_count_test: number of elements in each class in the testing set
        # - length_Xtrain: number of elements in the training set
        # - length_Xtest: number of elements in the testing set
        # - length_ytrain: number of labels in the training set
        # - length_ytest: number of labels in the testing set
        # - max_Xtrain: maximum value in the training set
        # - max_Xtest: maximum value in the testing set

        # return values:
        # Xtrain, ytrain, Xtest, ytest: the data used to fill the `answer`` dictionary

        Xtrain, ytrain, Xtest, ytest = u.prepare_data()
        Xtrain = nu.scale_data(Xtrain)
        Xtest = nu.scale_data(Xtest)

        nb_classes_train,nb_classes_test,class_count_train,class_count_test,length_Xtrain,length_Xtest,length_ytrain,length_ytest,max_Xtrain,max_Xtest = nu.eda(Xtrain,Xtest,ytrain,ytest)
        
        answer["nb_classes_train"] = nb_classes_train
        answer["nb_classes_test"] = nb_classes_test
        answer["class_count_train"] = class_count_train
        answer["class_count_test"] = class_count_test
        answer["length_Xtrain"] = length_Xtrain
        answer["length_Xtest"] = length_Xtest
        answer["length_ytrain"] = length_ytrain
        answer["length_ytest"] = length_ytest
        answer["max_Xtrain"] = max_Xtrain
        answer["max_Xtest"] = max_Xtest

        return answer, Xtrain, ytrain, Xtest, ytest

    """
    B.  Repeat part 1.C, 1.D, and 1.F, for the multiclass problem. 
        Use the Logistic Regression for part F with 300 iterations. 
        Explain how multi-class logistic regression works (inherent, 
        one-vs-one, one-vs-the-rest, etc.).
        Repeat the experiment for ntrain=1000, 5000, 10000, ntest = 200, 1000, 2000.
        Comment on the results. Is the accuracy higher for the training or testing set?
        What is the scores as a function of ntrain.

        Given X, y from mnist, use:
        Xtrain = X[0:ntrain, :]
        ytrain = y[0:ntrain]
        Xtest = X[ntrain:ntrain+test]
        ytest = y[ntrain:ntrain+test]
    """

    def partB(
        self,
        X: NDArray[np.floating],
        y: NDArray[np.int32],
        Xtest: NDArray[np.floating],
        ytest: NDArray[np.int32],
        ntrain_list: list[int] = [],
        ntest_list: list[int] = [],
    ) -> dict[int, dict[str, Any]]:
        """ """
        # Enter your code and fill the `answer`` dictionary
        Xtrain, ytrain, Xtest, ytest = u.prepare_data()
        Xtrain = nu.scale_data(Xtrain)
        Xtest = nu.scale_data(Xtest)


        answer = {}
        # 1000
        ntrain = 1000
        ntest = 200
        answer[ntrain] = {}
        answer[ntrain]["partC"] = nu.part1_partC(self.seed,ntrain,Xtrain,ytrain)
        answer[ntrain]["partD"] = nu.part1_partD(self.seed,ntrain,Xtrain,ytrain)
        answer[ntrain]["partF"] = nu.part1_partF(self.seed,ntrain,Xtrain,ytrain)
        answer[ntrain]["ntrain"] = len(Xtrain[0:ntrain, :])
        answer[ntrain]["ntest"] = len(Xtest[0:ntest, :])
        answer[ntrain]["class_count_train"] = nu.value_counts(ytrain[0:ntrain])
        answer[ntrain]["class_count_test"] = nu.value_counts(ytest[0:ntest])

        # 5000
        ntrain = 5000
        ntest = 1000

        answer[ntrain] = {}
        answer[ntrain]["partC"] = nu.part1_partC(self.seed,ntrain,Xtrain,ytrain)
        answer[ntrain]["partD"] = nu.part1_partD(self.seed,ntrain,Xtrain,ytrain)
        answer[ntrain]["partF"] = nu.part1_partF(self.seed,ntrain,Xtrain,ytrain)
        answer[ntrain]["ntrain"] = len(Xtrain[0:ntrain, :])
        answer[ntrain]["ntest"] = len(Xtest[0:ntest, :])
        answer[ntrain]["class_count_train"] = nu.value_counts(ytrain[0:ntrain])
        answer[ntrain]["class_count_test"] = nu.value_counts(ytest[0:ntest])

        # 10000
        ntrain = 10000  
        ntest = 2000
        answer[ntrain] = {}
        answer[ntrain]["partC"] = nu.part1_partC(self.seed,ntrain,Xtrain,ytrain)
        answer[ntrain]["partD"] = nu.part1_partD(self.seed,ntrain,Xtrain,ytrain)
        answer[ntrain]["partF"] = nu.part1_partF(self.seed,ntrain,Xtrain,ytrain)
        answer[ntrain]["ntrain"] = len(Xtrain[0:ntrain, :])
        answer[ntrain]["ntest"] = len(Xtest[0:ntest, :])
        answer[ntrain]["class_count_train"] = nu.value_counts(ytrain[0:ntrain])
        answer[ntrain]["class_count_test"] = nu.value_counts(ytest[0:ntest])

        # the accuracy scores increase as a function of n-train. The highest accuracy is observed for Logistic regression

        """
        `answer` is a dictionary with the following keys:
           - 1000, 5000, 10000: each key is the number of training samples

           answer[k] is itself a dictionary with the following keys
            - "partC": dictionary returned by partC section 1
            - "partD": dictionary returned by partD section 1
            - "partF": dictionary returned by partF section 1
            - "ntrain": number of training samples
            - "ntest": number of test samples
            - "class_count_train": number of elements in each class in
                               the training set (a list, not a numpy array)
            - "class_count_test": number of elements in each class in
                               the training set (a list, not a numpy array)
        """

        return answer
