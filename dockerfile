FROM python
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install gspread
RUN pip3 install scikit-learn
RUN pip3 install numpy
COPY excell_bet2.py /opt/excell_bet2.py
CMD ['python3', 'excell_bet2.py']