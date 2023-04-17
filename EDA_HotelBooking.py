#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('dark_background')


# In[3]:


df = pd.read_csv


# In[1]:


df = pd.read_csv('C:\\Users\\Ekta\\Downloads\\hotel_bookings 2.csv')


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('dark_background')


# In[3]:


df = pd.read_csv('C:\\Users\\Ekta\\Downloads\\hotel_bookings 2.csv')


# In[4]:


df.read()


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.tail(20)


# In[8]:


df.info()


# In[10]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[11]:


for col in df.describe(include = 'object'). columns:
    print(col)
    print(df[col].unique())


# In[12]:


for col in df.describe(include = 'object'). columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[13]:


df.isnull().sum()


# In[14]:


df.drop(['company', 'agent'], axis = 1, inplace = True)
df.dropna(inplace = True)


# In[15]:


df.isnull().sum()


# In[16]:


df.describe()


# In[18]:


df['adr'].plot(kind = 'box')


# In[19]:


df = df[df['adr']<5000]


# In[20]:


df.describe()


# In[22]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)


# In[23]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
cancelled_perc


# In[29]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print(cancelled_perc)

plt.figure(figsize = (5,4))
plt.title('Reservation Status Count')
plt.bar(['Not canceled', 'Canceled'], df['is_canceled'].value_counts())
plt.show()


# In[30]:


resort_hotel = df[df['hotel'] == 'Resort hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[31]:


Hotel_typ = df['hotel'].value_counts()
Hotel_typ


# In[32]:


plt.subplot(2,2,1 )
Hotel_typ.plot.pie(x='City Hotel', y ='Resort Hotel',autopct='%1.0f%%',textprops={'weight': 'bold'},figsize =(12,12),explode =[0.05]*2) 
plt.title('Hotel type',fontweight="bold", size=20)

#--------------------------------------------------------------------------------------------------#
plt.subplot(2,2,2 )
meal_typ =df['meal'].value_counts()
meal_typ.plot.pie(autopct='%1.0f%%',textprops={'weight': 'bold'},explode = [0.05]*5)
plt.title('Favourite food type',fontweight="bold", size=20)
#--------------------------------------------------------------------------------------------------# 
plt.subplot(2,2,3 )
booking_distibution_typ = df['distribution_channel'].value_counts()
booking_distibution_typ.plot.pie(autopct='%.2f%%',textprops={'weight': 'bold'}, pctdistance=0.5,explode = [0.05]*5)
plt.title('Booking % by distribution channel', fontweight ='bold', size =20);
#--------------------------------------------------------------------------------------------------#
plt.subplot(2,2,4)
Repeated = df.is_repeated_guest .value_counts()
Repeated.plot.pie(autopct='%1.0f%%',textprops={'weight': 'bold'},explode = [0.05]*2)
plt.title('Repeated guests', fontweight ='bold', size =20);


# In[37]:


df['Full_stay'] = df.stays_in_weekend_nights + df.stays_in_week_nights
plt.figure(figsize = (12,6))
sns.scatterplot(y = 'adr', x = 'Full_stay', data = df)
plt.show()


# In[38]:


df['Total_members'] = df.adults + df.children + df.babies
df.loc[df.Total_members > 20, 'Total_members'] = 20


# In[39]:


df.info()


# In[42]:


City_df =pd.DataFrame(df[df['hotel'] =='City Hotel'])
Resort_df =pd.DataFrame(df[df['hotel'] =='Resort Hotel'])


# In[43]:


Corr_df = df[['lead_time','previous_cancellations','previous_bookings_not_canceled','booking_changes','days_in_waiting_list','adr','required_car_parking_spaces','total_of_special_requests']]


# In[44]:


corr_mat = df.corr()
f, ax = plt.subplots(figsize=(12, 7))
sns.heatmap(corr_mat,vmax=0.8,annot = True,fmt='.2f');


# In[45]:


np.warnings.filterwarnings('ignore')
df['Total_members'] = df.adults + df.children + df.babies
df.loc[df.Total_members > 20, 'Total_members'] = 20


# In[46]:


df.info()


# In[48]:


Corr_df = df[['lead_time','previous_cancellations','previous_bookings_not_canceled','booking_changes','days_in_waiting_list','adr','required_car_parking_spaces','total_of_special_requests', 'Total_members']]


# In[49]:


corr_mat = df.corr()
f, ax = plt.subplots(figsize=(12, 7))
sns.heatmap(corr_mat,vmax=0.8,annot = True,fmt='.2f');


# In[51]:


df.customer_type.nunique()
Customer_typ = df.customer_type .value_counts()
plt.figure(figsize =(12,12))
plt.subplot(1,2,1 )
Customer_typ.plot.pie(autopct='%1.0f%%',textprops={'weight': 'bold'},explode =[0.05]*4)
plt.title('Customer type',fontweight="bold", size=20)


# In[52]:


df.customer_type.nunique()
Customer_typ = df.customer_type .value_counts()
plt.figure(figsize =(12,12))
plt.subplot(1,2,1 )
Customer_typ.plot.pie(autopct='%1.0f%%', explode =[0.05]*4)
plt.title('Customer type',fontweight="bold", size=20)


# In[53]:


df.customer_type.nunique()
Customer_typ = df.customer_type .value_counts()
plt.figure(figsize =(12,12))
plt.subplot(1,2,1 )
Customer_typ.plot.pie(textprops={'weight': 'bold'},explode =[0.05]*4)
plt.title('Customer type',fontweight="bold", size=20)


# In[54]:


df.customer_type.nunique()
Customer_typ = df.customer_type .value_counts()
plt.figure(figsize =(12,12))
plt.subplot(1,2,1 )
Customer_typ.plot.pie(autopct='%1.0f%%',textprops={'weight': 'bold'})
plt.title('Customer type',fontweight="bold", size=20)


# In[57]:


plt.subplot(1,2,2)
Car_parking_spaces = df.required_car_parking_spaces.value_counts()
Car_parking_spaces.plot.pie(autopct='%1.0f%%',textprops={'weight': 'bold'})
plt.title('required_parking_spaces',fontweight="bold", size=20)


# # Hotel booking Date/Month wise

# In[62]:


City_df.arrival_date_month.value_counts()


# In[63]:


Resort_df.arrival_date_month.value_counts()


# In[64]:


plt.figure(figsize=(12,6))
sns.countplot(data = df, x = 'arrival_date_day_of_month', hue='hotel', palette='Paired')
plt.show()


# we can see less no. of arrivals are at the month end.

# In[65]:


resort_guest = Resort_df['arrival_date_month'].value_counts().reset_index() 
resort_guest.columns=['month','no of guests']
resort_guest

city_guest = City_df['arrival_date_month'].value_counts().reset_index()
city_guest.columns=['month','no of guests']
city_guest

final_guest=resort_guest.merge(city_guest, on = 'month')                              #merge resort guest and city guest month wise
final_guest.columns=['month','no of guests in resort','no of guest in city hotel']
final_guest
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
final_guest['month'] = pd.Categorical(final_guest['month'], categories=months, ordered=True)

#Which month get most visitors?
plt.figure(figsize =(15,8))
sns.lineplot(data=final_guest, x='month', y='no of guests in resort', marker ='^')
sns.lineplot(data=final_guest, x='month', y='no of guest in city hotel',marker ='^')
plt.legend(['Resort','City Hotel'])
plt.ylabel('Number of guest')


# May, June, July, August have most visitors

# # From where most visitors are coming from

# In[66]:


plt.figure(figsize = (10,5))

sns.barplot (y= list(df.country.value_counts().head (10)), x= list(df.country.value_counts().head(10).index))
plt.title("Number of bookings country wise",fontweight="bold", size=20)


# # Adults and Kids

# In[69]:


df['kids'] = df.children + df.babies
df['kids'].value_counts()


# In[71]:


df['adults'].value_counts()


# In[72]:


df.loc[df.Total_members > 20, 'Total_members'] = 20   #removing outlier from Total_members column
plt.figure(figsize=(10,6))
sns.countplot(df['Total_members'], palette='husl')
plt.show()


# Most people prefer coming in 2

# In[76]:


plt.figure(figsize = (20,7))
plt.subplot(1,2,1)
sns.countplot( x = df['assigned_room_type'])
plt.title('Preferred room types',fontweight="bold", size=20)
plt.subplot(1,2,2)
sns.boxplot(x = df['assigned_room_type'], y = df['adr'])


# Room type A and D are most preferred by guests.
# 
# but better 'Average daily rate' rooms are of type H,G,F and C.

# # Stay Length in Hotels

# In[78]:


not_canceled = df[df['is_canceled'] == 0]
s1 = not_canceled[not_canceled['Full_stay'] < 15] 
plt.figure(figsize = (10,5))
sns.countplot(x = s1['Full_stay'], hue = s1['hotel'])
plt.title('Stay length in hotels',fontweight="bold", size=20)


# Most common stay length is less than 4 days and generally people prefer City hotel for short stay, but for long stays, Resort Hotel is preferred.
# 
# 

# In[79]:


plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1)
sns.countplot(x='stays_in_weekend_nights',hue='hotel', data=df, palette='cool')
plt.title("Number of stays on weekend nights",fontweight="bold", size=20)
plt.subplot(1, 2, 2)
sns.countplot(x='stays_in_week_nights',hue='hotel', data=df, palette='rainbow_r')
plt.title("Number of stays on weekday nights",fontweight="bold", size=20)


# city hotels have more number of stays irrespective of week or weekend stays.
# 
# 

# # Cancellation Rate

# In[80]:


plt.figure(figsize = (10,5))
sns.countplot(x='deposit_type',data=df,hue ='is_canceled')
plt.title('Booking preferred with deposite type',fontweight ="bold",size =10)


# As expected , Most Bookings are done with 'No deposite' and most cancellations are also in 'no deposit' bookings. It is a surprise to see cancellations with 'Non-refundable' bookings

# # Average Daily Rate- Month wise

# In[81]:


plt.figure(figsize=(12,5))
sns.lineplot(data = df, x = 'arrival_date_month', y = 'adr', hue = 'hotel',sort =True, marker ='^')
plt.title('Average daily rate month wise',fontweight ='bold',size =20)


# In[ ]:


For resort hotels, the average daily rate is more expensive during august, july and september.

For city hotels, the average daily rate is more expensive during august, july, june and may.


# # Special Requests

# In[82]:


df['total_of_special_requests'].value_counts()


# In[83]:


plt.figure(figsize =(10,6))
sns.countplot(data = df,x ='total_of_special_requests', hue ='hotel')
plt.xlabel('No. of special requests')


# City hotels have more no. of special requests. Most of them ask for only 1 special request.
# 
# 

# In[84]:


df.Total_members.sum()


# 234163 total members have been registered in the hotels
# 
# 

# In[85]:


df.required_car_parking_spaces.sum()


# 7358 car Parking spaces have been used
# 
# 

# The majority of guests come from western europe countries.We should spend a significant amount of our budget on those area.
# 
# 80% distribution_channel is TA/TO
# 
# Around 61% bookings are for City hotel and 39% bookings are for Resort hotel, therefore City Hotel is busier than Resort hotel.
# 
# Given that we do not have repeated guests, we should target our advertisement on guests to increase returning guests.
# 
# Majority of the hotels booked are city hotel. Definitely need to spend the most targeting fund on those hotel.
# 
# Most common stay length is less than 4 days and generally people prefer City hotel for short stay, but for long stays, Resort Hotel is preferred.
# 
# 
