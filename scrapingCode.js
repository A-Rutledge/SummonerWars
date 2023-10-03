//If you go into a completed game, right click, inspect, and go to the "Console" tab, you can paste this and it will export the file for you.
//Line break separated:
//------------------------------------------------------------------
const logEntries = [];
//looks in the "full-log" portion of the DOM and for every entry trims the text and adds it to the logEntries array
const fullLog = document.querySelector('#full-log');
for (let i=0; i < fullLog.children.length; i++) {
    const logEntry = fullLog.children[i].textContent.trim();
    if(logEntry) {
        logEntries.push(logEntry);
    }
}

//the data comes in newline separated, so this joins on the \n character
const csvContent = logEntries.join('\n');


//writes the data to a csv file on click
const blob = new Blob([csvContent], { type: 'text/csv' });
const link = document.createElement('a');
link.href = URL.createObjectURL(blob);
link.download = 'game_log.csv';


link.click();
