##### Development Log

#### Develop SQLite.

SubTask-1: Learn about SQLite. The official website is https://www.sqlite.org/. Most SQL dataset is Client/Server designed, but SQLite is different, it is sort of file system design. All the data of databases is saved in the file. 

The interaction of using sqlite is command sqlite3. When I typed **sqlite3** in the interaction command, there is one transient in-memory database appears. Such command can also be integrated in other scripts. 

#### Create one database having frame of index, word, pronunciation, explanation and example. 

The data could be imported from CSV. Therefore, the word scheme should be managed and operated using excel software. Therefore, the learnt word should be organized in one CSV file firstly. This part is for data storage. 

The CSV file can have header, and the first line of the file is the header. 