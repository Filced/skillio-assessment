
create table person if not exist(
    id serial primary key,
    name varchar(100),
    age int,
    student boolean
);

insert into person (name, age, student) values ('Alice', 20, true);
insert into person (name, age, student) values ('Bob', 21, false);
insert into person (name, age, student) values ('Charlie', 22, true);
insert into person (name, age, student) values ('David', 23, false);
insert into person (name, age, student) values ('Eve', 24, true);

create table certificates (
    id serial primary key,
    name varchar(100) not null,
    person_id int,
    CONSTRAINT fk_person 
        FOREIGN KEY( person_id ) 
            REFERENCES person(id)
);

insert into certificates (name, person_id) values ('Scrum', 1);
insert into certificates (name, person_id) values ('Python', 1);
insert into certificates (name, person_id) values ('Scrum', 2);
insert into certificates (name, person_id) values ('Azure Data Engineer', 2);
insert into certificates (name, person_id) values ('Azure Data Engineer', 3);
insert into certificates (name, person_id) values ('AWS Solutions Architect Professional', 4);
