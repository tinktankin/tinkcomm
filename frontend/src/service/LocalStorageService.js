const LocalStorageService = (function(){
    let _service;
    function _getService() {
        if(!_service) {
          _service = this;
          return _service
      }
      return _service
    }
    function _setToken(token) {
      localStorage.setItem(btoa("access-token"), token);
    }
    function _getAccessToken() {
      return localStorage.getItem(btoa("access-token"));
    }
    
    function _clearToken() {
      localStorage.removeItem(btoa("access-token"));
    }
   return {
      getService : _getService,
      setToken : _setToken,
      getAccessToken : _getAccessToken,
      clearToken : _clearToken
    }
   })();
   export default LocalStorageService;