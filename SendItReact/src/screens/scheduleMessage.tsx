import React, {useState} from 'react';
import { SafeAreaView, Text, View, Button, Alert } from 'react-native';
import  ScheduleMessageForm  from '../components/sendMessageForm';

function ScheduleMessageScreen(): JSX.Element {
    
    const [showForm, setShowForm] = useState(false);
    
    const toggleForm = () => {
        setShowForm(!showForm);
    }

    return (
        <View>
            <Text>
                This is the schedule message screen. You'll input the recipient phone number, name, date/time to send the message, and the message itself.
            </Text>
            <Button
                title="Schedule Message"
                onPress={toggleForm}></Button>
            {showForm && <ScheduleMessageForm/>}
        </View>
    );

}

export default ScheduleMessageScreen;