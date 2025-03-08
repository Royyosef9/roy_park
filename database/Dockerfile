FROM postgres:15-alpine

# קביעת משתני סביבה
ENV POSTGRES_DB=parking_db
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=MyStrongPassword

# הוספת קובץ יצירת טבלאות ראשוני
COPY init.sql /docker-entrypoint-initdb.d/init.sql

EXPOSE 5432
CMD ["postgres"]
