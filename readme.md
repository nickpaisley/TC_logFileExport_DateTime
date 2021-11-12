## <p align='center'>Welcome to the Log File Export /w Date Time Script!</p>


### Premise and Operation

Customer requested a way to export Log Files in .MHT format with the date and time attached direclty to a specific folder on the client machine HD to help keep track of tests and logs. 


This was accomplished by created a Python script that uses *aqDateTime* to retrieve the current time. *aqConvert* was used to convert the inital time value created to a format compatible with Windows file naming conventions. After the time is retrieved and converted, we create a variable that contains the desired save location and formatted file name. Last step is pushing the file name up to the internal TC Log and then saving it directly to the hd.