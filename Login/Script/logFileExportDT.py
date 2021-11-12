def exportTestLog():
  
  # set a variable containing the current Date and Time. 
  aqTimeStamp = aqDateTime.Now()
  
  #format the new variable with correct characters for file creation
  dtForExport = aqConvert.DateTimeToFormatStr(aqTimeStamp, "%Y-%m-%d_%H%M%S")
  
  # set a variable building out the location to save the log file and the date/time.
  # to change the save directory just alter the path below in the first set of quotes.
  logFile = ("C:\Temp\TestComplete_Projects\Results" + "/" + dtForExport + ".mht")
  
  # add date/time output to the test log
  Log.Message(dtForExport)
  
  # export the log file from the keyword test or execution plan
  Log.SaveResultsAs(logFile, lsMHT)