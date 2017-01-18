import unittest

class Test_Foo(unittest.TestCase):
    '''Sample test case -- Test_Foo()'''
    
    def setUp(self):
        '''Set up for testing...'''
        print 'Test_Foo:setUp_:begin'
         
        testName = self.shortDescription()
        if (testName == 'Test routine A'):
            print 'setting up for test A'
        elif (testName == 'Test routine B'):
            print 'setting up for test B'
        else:
            print 'UNKNOWN TEST ROUTINE'
             
        print 'Test_Foo:setUp_:end'
        
    def testA(self):
        '''Test routine A'''
        print 'Test_Foo: running testA...'
        
    def testB(self):
        '''Test routine B'''
        print 'Test_Foo: running testB...'
        
    def tearDown(self):
        '''Tear down from testing...'''
        print 'Test_Foo:tearDown_:begin'
         
        testName = self.shortDescription()
        if (testName == 'Test routine A'):
            print 'cleaning up after test A'
        elif (testName == 'Test routine B'):
            print 'cleaning up after test B'
        else:
            print 'UNKNOWN TEST ROUTINE'
             
        print 'Test_Foo:tearDown_:end'
        
class BarTest(unittest.TestCase):
    '''Sample test case -- BarTest()'''
    
    def setUp(self):
        '''Set up for testing...'''
        print 'BarTest:setUp_:begin'
         
        testName = self.shortDescription()
        if (testName == 'Test routine A'):
            print 'setting up for test A'
        elif (testName == 'Test routine B'):
print 'setting up for test B'