(function(window, undefined) {
  var dictionary = {
    "df929bd9-7ff3-4ae0-a793-ed6398b679b7": "StatView",
    "01de8dc3-c48f-4553-911e-d84823348ec5": "MapView",
    "d12245cc-1680-458d-89dd-4f0d7fb22724": "Test Screen",
    "e73b655d-d3ec-4dcc-a55c-6e0293422bde": "960 grid - 16 columns",
    "ef07b413-721c-418e-81b1-33a7ed533245": "960 grid - 12 columns",
    "f39803f7-df02-4169-93eb-7547fb8c961a": "Template 1",
    "aa0b8f30-ab7d-4a70-b9ba-1c353205db72": "MapView  StatView",
    "5d1cb25b-ae81-466d-ad67-c27a15ae02b6": "SideMenu",
    "add2bb81-e012-430e-825a-53aae0e57db4": "HomeScreen ReportBox",
    "5e1bd681-ee9a-401d-a3d0-d207ef29eae8": "Header",
    "57eb3f77-bfe0-4694-8272-0f4da514ea8d": "StatView MapView",
    "bb8abf58-f55e-472d-af05-a7d1bb0cc014": "default"
  };

  var uriRE = /^(\/#)?(screens|templates|masters|scenarios)\/(.*)(\.html)?/;
  window.lookUpURL = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, url;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      url = folder + "/" + canvas;
    }
    return url;
  };

  window.lookUpName = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, canvasName;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      canvasName = dictionary[canvas];
    }
    return canvasName;
  };
})(window);