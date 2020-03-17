pragma solidity ^0.5.1;

contract Greetings {

    string public greeting;

    constructor () public {
        greeting = "Hello World";
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    function getGreeting() public view returns (string memory greetings){
        return greeting;
    }
}