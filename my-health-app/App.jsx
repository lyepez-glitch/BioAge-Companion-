import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import LoginScreen from './LoginScreen';
import RegisterScreen from './RegisterScreen';
import ProfileSetupScreen from './ProfileSetupScreen';
import HealthMetricsScreen from './HealthMetricsScreen';
import BiologicalAgeScreen from './BiologicalAgeScreen';
import RecommendationsScreen from './RecommendationsScreen';

const Stack = createNativeStackNavigator();

export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator initialRouteName="Register">
                <Stack.Screen name="Login" component={LoginScreen} />
                <Stack.Screen name="Register" component={RegisterScreen} />
                <Stack.Screen name="ProfileSetup" component={ProfileSetupScreen} />
                <Stack.Screen name="HealthMetrics" component={HealthMetricsScreen} />
                <Stack.Screen name="BiologicalAge" component={BiologicalAgeScreen} />
                <Stack.Screen name="Recommendations" component={RecommendationsScreen} />
            </Stack.Navigator>
        </NavigationContainer>
    );
}
