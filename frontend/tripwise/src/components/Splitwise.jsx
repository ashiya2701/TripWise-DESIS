import React from "react";
import Logout from './Logout';
import CreateGroup from './create_group'
import GroupList from './list_groups';

function Splitwise(){

    return (
        <div>
            <CreateGroup/>
            <GroupList/>
            <Logout/>
        </div>
        
    );
}

export default Splitwise;