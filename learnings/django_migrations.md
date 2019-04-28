### DJANGO MIGRATIONS

#### Uses
1. Schema is made without writing sql
2. Model and schema are in sync

#### Operation
1. You can apply, and also restore migrations. For restore to an older migrations 
simply write the app name followed by the migrations you want to restore to.

2. Django keeps track of all migration in the django_migrations table.
A row is inserted in when we run migrations, or fake migrations. This is
why changing of migration file which has been already applied has no effect 
when migrations are run again.

3. Use fake, when you want to tell django to update the django_migrations, but
not actually do any changes in the database itself. Use this incase of
conflicts.

4. To undo all migrations, we can use makemigrations zero. This will fake
migrations can be very useful in solving conflicts.

5. Migrations can also be used to alter data - Data Migrations (Seperate topic)








#### Commands
    1. showmigrations - List all migrations
    
    



