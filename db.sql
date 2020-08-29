create database collegeweb;

create table collegeweb.user(
    userid int AUTO_INCREMENT,
    username varchar(100) NOT NULL,
    email varchar(50) NOT NULL UNIQUE,
    password varchar(12) NOT NULL,
    type int NOT NULL,/*Faculty:1, Stduent:2*/
    branch int NOT NULL,/*CS:1,ME:2*/    
    PRIMARY KEY(userid)
);

create table collegeweb.question(
    qid int AUTO_INCREMENT,
    student int,
    qus varchar(1000),
    PRIMARY KEY(qid)
);