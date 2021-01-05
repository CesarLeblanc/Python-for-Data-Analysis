# Python-for-Data-Analysis

## I. Presentation of our Dataset :

The problem consists in classifying all the blocks of the page layout of a document that has been detected by a segmentation process. This is an essential step in document analysis in order to separate text from graphic areas. Indeed, the five classes are: text (1), horizontal line (2), picture (3), vertical line (4) and graphic (5).

The 5473 examples comes from 54 distinct documents. Each observation concerns one block. All attributes are numeric. Data are in a format readable by C4.5. There is no missing value.

The features of the dataset are : 

height:   integer.         | Height of the block.
lenght:   integer.     | Length of the block.   
area:     integer.    | Area of the block (height * lenght).    
eccen:    continuous.  | Eccentricity of the block (lenght / height).  
p_black:  continuous.  | Percentage of black pixels within the block (blackpix / area).  
p_and:    continuous.        | Percentage of black pixels after the application of the Run Length Smoothing Algorithm (RLSA) (blackand / area).  
mean_tr:  continuous.      | Mean number of white-black transitions (blackpix / wb_trans).  
blackpix: integer.    | Total number of black pixels in the original bitmap of the block.  
blackand: integer.        | Total number of black pixels in the bitmap of the block after the RLSA.  
wb_trans: integer.          | Number of white-black transitions in the original bitmap of the block.  


## II. Results :

We started by doing a healthcheck to see if we had any missing values, NA or NULL and we did some data visualizations. 

We did five steps of modelling: 

- The first one was with raw data, without pre-processing. We tried different models that we had seen in Machine Learning, such as: Logistic Regression, Support Vector Machine, K-Nearest Neighbours, Decision Tree, Random Forest, Bagging, ADA Boost. We decided to only keep the 3 models with the best accuracy: Decision Tree, Random Forest and ADA Boost.

- The second step was with pre-processing. We explored the correlation of all features to the target and decided to remove the 3 least correlated features: lenght, mean_tr and wb_trans. We used the same 3 models that we kept previously. 

- The third step was the same as second step but with scaling.

- The fourth step was the same as the third step but while tuning the hyperparameters. 

- In the fifth step we added cross validation. 


At the end, our best accuracy was with the model Random Forest and we got 98.4% of accuracy. 

## III. Our Flask webapp :

How to properly launch our Flask wepp : download the folders "static/images", "data" and "templates" and the file "app.py" and put them all in the same folder.

Next, launch the file "app.py" and make sure that you have all the needed libraries.

Run the program, and click on the link that will appear on your console ("http://127.0.0.1:5000/").

You can try to predict the type of a page block based on the seven most important variables and by choosing one of our three best models (Decision Tree, Random Forest and ADA Boost which all have ~98% accuracy).

You can try with different data as much as you want by clicking "Clear" or "Reset".

You can also check the full dataset by clicking "View Dataset".

Last but not least, you can check a summary of the problem by clicking "Summary".
